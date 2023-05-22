module Jekyll
  module VideoLibrary

    def slack_channel_name(path)
      if path.nil?
        return "general"
      end
      path_parts = path.split('/')

      # Update these two terms, just overwriting them
      if path_parts[0] == 'statistics'
        path_parts[0] = 'machine_learning'
      end

      if path_parts[0] == 'sequence-analysis'
        path_parts[0] = 'ngs'
      end

      if path =~ /olympic/
        return path_parts[0..1].join("_")
      end

      if path.include?('galaxy/intro') or path_parts[0] == 'introduction'
        return 'galaxy-intro'
      elsif path_parts[0] == 'galaxy-interface'
        return path_parts[0..1].join("_")
      elsif ['galaxy', 'community', 'webinar'].include? path_parts[0]
        return 'general'
      elsif path_parts[0] == 'course'
        # These are specific to their events
        return ['event', path_parts[1].gsub(/welcome-/, '')].join('-')
      elsif path_parts[0] == 'contributing'
        return 'gtn'
      elsif path_parts[1].include?('tool-generators')
        return 'dev-toolfactory'
      elsif path_parts.length > 2 and ['tutorial', 'slides'].include?(path_parts[2])
        return path_parts[0..1].join("_")
      elsif path_parts.length > 2
        return path_parts[0..1].join("_")
      elsif path_parts.length == 2
        path_parts[0..1].join("_")
      else
        return "general"
      end
    end

    def duration_to_human(duration)
      # Match the different parts of the string, must match entire string or it will fail.
      match = /^(?:([0-9]*)[Hh])*(?:([0-9]*)[Mm])*(?:([0-9.]*)[Ss])*$/.match(duration)

      # If it doesn't match, pass through unedited so we don't cause unexpected issues.
      if match.nil? then
        puts "Could not parse time: #{duration}"
        return duration
      end

      # Otherwise append english terms for the various parts
      duration_parts = []

      hour = "hour"
      hours = "hours"
      minutes = "minutes"
      if @context.registers[:page]&.key?('lang')
          lang = @context.registers[:page]['lang']
          hour = @context.registers[:site].data["lang"][lang]["hour"]
          hours = @context.registers[:site].data["lang"][lang]["hours"]
          minutes = @context.registers[:site].data["lang"][lang]["minutes"]
      end

      # Hours
      if ! match[1].nil? then
        if match[1] == '1' then
          duration_parts.push("#{match[1]} "+hour)
        else
          duration_parts.push("#{match[1]} "+hours)
        end
      end

      # Minutes - assuming no one uses `1 minute`
      if ! match[2].nil? then
        duration_parts.push("#{match[2]} "+minutes)
      end

      # Hopefully no one uses seconds
      if ! match[3].nil? then
        duration_parts.push("#{match[3]} seconds")
      end

      return duration_parts.join(' ')
    end
  end
end

Liquid::Template.register_filter(Jekyll::VideoLibrary)
