require 'json'

module Jekyll
  class APIGenerator < Generator

    def generate(site)
      puts "[VideoLibrary/API] Videos"
      page2 = PageWithoutAFile.new(site, "", "api/", "videos.json")
      page2.content = JSON.pretty_generate(site.data['videos'])
      page2.data["layout"] = nil
      site.pages << page2

      by_tags = Hash.new { |hash, key| hash[key] = Hash.new }
      site.data['videos'].each{|k, v|
        v['tags'].each{|tag|
          by_tags[tag]['url'] = site.config['baseurl'] + "/api/tags/#{tag}.json"
          if by_tags[tag]['videos'].nil?
            by_tags[tag]['videos'] = Hash.new
          end
          by_tags[tag]['videos'][k] = v
        }
      }

      by_tags.each{ |tag, data|
        page2 = PageWithoutAFile.new(site, "", "api/", "tags/#{tag}.json")
        page2.content = JSON.pretty_generate(data)
        page2.data["layout"] = nil
        site.pages << page2
      }

      page2 = PageWithoutAFile.new(site, "", "api/", "tags.json")
      page2.content = JSON.pretty_generate(by_tags)
      page2.data["layout"] = nil
      site.pages << page2

    end
  end
end

