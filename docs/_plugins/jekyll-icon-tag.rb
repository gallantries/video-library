module Jekyll
  class IconTag < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
      parts = text.strip.split
      @text = parts[0]
      @aria = true
      if parts[1] == 'aria=false' then
        @aria = false
      end
    end

    def render_for_text(icon, cfg)
      if icon.empty?
        raise SyntaxError.new(
          "No icon defined for: '#{@text}'. " +
          "Please define it in `_config.yml` (under `icon-tag:`)."
        )
      end

      if icon.start_with?("fa")
        if @aria
          %Q(<i class="#{icon}" aria-hidden="true"></i><span class="visually-hidden">#{@text}</span>)
        else
          %Q(<i class="#{icon}" aria-hidden="true"></i>)
        end
      elsif icon.start_with?("ai")
        if @aria
          %Q(<i class="ai #{icon}" aria-hidden="true"></i><span class="visually-hidden">#{@text}</span>)
        else
          %Q(<i class="ai #{icon}" aria-hidden="true"></i>)
        end
      elsif icon.start_with?("assets/fa/")
        if @aria
          %Q(<img style="height: 1em" src="#{cfg['baseurl']}/#{icon}" alt="#{icon}" aria-hidden="true"/>)
        else
          %Q(<img style="height: 1em" src="#{cfg['baseurl']}/#{icon}" alt="#{icon}" aria-hidden="true"/>)
        end
      end
    end

    def render(context)
      cfg = get_config(context)
      icon = cfg['icon-tag'][@text] || ''
      render_for_text(icon, cfg)
    end

    def get_config(context)
      context.registers[:site].config
    end
  end
end

Liquid::Template.register_tag('icon', Jekyll::IconTag)
