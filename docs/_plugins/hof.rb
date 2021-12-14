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
      captions_by_author= Hash.new { |hash, key| hash[key] = [] }

      site.data['videos'].each{|k, v|
        if ! v.nil?
          k2 = k.split('/')[0,2].join('/')

          name = site.data['gtn'].fetch(k2, k2)

          v.fetch('versions', []).each{|version|
            version['speakers'].each{|speaker|
              videos_by_author[speaker].push([k, name, version])
            }
            if version['captions']
              version['captions'].each{|speaker|
                captions_by_author[speaker].push([k, name, version])
              }
            end
          }
        end
      }

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

        page2.data["videos_count"] = videos_by_author[contributor].length
        page2.data["caption_count"] = captions_by_author[contributor].length

        page2.data["videotime"] = site.data['stats']['byspeaker'][contributor]
        page2.data["captiontime"] = site.data['stats']['bycaptioner'][contributor]

        site.pages << page2
      end
    end
  end
end
