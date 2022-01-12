module Jekyll
  class AuthorPageGenerator < Generator
    safe true

    def findDuration(duration)
      eval(duration.gsub(/H/, ' * 3600 + ').gsub(/M/, ' * 60 + ').gsub(/S/, ' + ') + " 0")
    end

    def generate(site)
      if ! site.layouts.key? 'contributor_index'
        return
      end

      videos_by_author = Hash.new { |hash, key| hash[key] = [] }
      events_by_author = Hash.new { |hash, key| hash[key] = [] }
      captions_by_author = Hash.new { |hash, key| hash[key] = [] }

      site.data['videos'].each{|k, v|
        if ! v.nil?
          v.fetch('versions', []).each{|version|
            version['speakers'].each{|speaker|
              videos_by_author[speaker].push([k, version])
            }
            if version['captions']
              version['captions'].each{|speaker|
                captions_by_author[speaker].push([k, version])
              }
            end
          }
        end
      }

      site.pages.select{|p| p['layout'] == 'event'}.each do |event|
        event.data['instructors'].each do |person|
          events_by_author[person].push(event)
        end
      end

      site.data['instructor_keys'] = site.data['instructors'].keys
      site.data['instructors'].each_key do |contributor|
        page2 = PageWithoutAFile.new(site, "", File.join('contributors', contributor), "index.html")
        page2.content = nil
        name = site.data['instructors'][contributor].fetch('name', contributor)

        # Their tutorials
        page2.data["contributor"] = contributor
        page2.data['personname'] = name
        page2.data['title'] = "GTN Video Library Contributor: #{name}"
        page2.data["layout"] = "contributor_index"

        page2.data["videos"] = videos_by_author[contributor]
        page2.data["caption"] = captions_by_author[contributor]
        page2.data["events"] = events_by_author[contributor].select{|e| ! e.data['example'] }.map{|e| e.data.update({"url" => e.url}) }.uniq

        page2.data["events_count"] = events_by_author[contributor].length
        page2.data["videos_count"] = videos_by_author[contributor].length
        page2.data["caption_count"] = captions_by_author[contributor].length

        site.pages << page2
      end
    end
  end
end
