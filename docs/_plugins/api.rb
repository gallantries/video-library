require 'json'

module Jekyll
  class APIGenerator < Generator

    def findDuration(duration)
      eval(duration.gsub(/H/, ' * 3600 + ').gsub(/M/, ' * 60 + ').gsub(/S/, ' + ') + " 0")
    end

    def generate(site)
      puts "[VideoLibrary/API] Videos"
      page2 = PageWithoutAFile.new(site, "", "api/", "videos.json")
      page2.content = JSON.pretty_generate(site.data['videos'])
      page2.data["layout"] = nil
      site.pages << page2

      by_tags = Hash.new { |hash, key| hash[key] = Hash.new }
      site.data['videos'].each{|k, v|
        if ! v.nil?
          v.fetch('tags', []).each{|tag|
            by_tags[tag]['url'] = site.config['baseurl'] + "/api/tags/#{tag}.json"
            if by_tags[tag]['videos'].nil?
              by_tags[tag]['videos'] = Hash.new
            end
            by_tags[tag]['videos'][k] = v
          }
        end
      }

      site.data['by_tags'] = by_tags
      by_tags.each{ |tag, data|
        page2 = PageWithoutAFile.new(site, "", "api/", "tags/#{tag}.json")
        page2.content = JSON.pretty_generate(data)
        page2.data["layout"] = nil
        site.pages << page2
      }

      by_material = Hash.new { |hash, key| hash[key] = Array.new }
      site.data['videos'].each{|k, v|
        if v && v['materials']
          v.fetch('materials', []).each{|material|
            if material['link'] && material['link'].start_with?('topics/')
              if v['versions']
                v['versions'].each{|vid|
                  by_material[material['link']].push(vid)
                }
              end
            end
          }
        end
      }

      by_material.each{ |tag, data|
        page2 = PageWithoutAFile.new(site, "", "api/", "by-material/#{tag}.json")
        page2.content = JSON.pretty_generate(data)
        page2.data["layout"] = nil
        site.pages << page2
      }
      page2 = PageWithoutAFile.new(site, "", "api/", "by-material.json")
      page2.content = JSON.pretty_generate(by_material)
      page2.data["layout"] = nil
      site.pages << page2

      page2 = PageWithoutAFile.new(site, "", "api/", "tags.json")
      page2.content = JSON.pretty_generate(by_tags)
      page2.data["layout"] = nil
      site.pages << page2

      # Stats
      durations = Hash.new { 0 }
      durations['bytag'] = Hash.new { 0 }
      durations['byspeaker'] = Hash.new { 0 }
      durations['bycaptioner'] = Hash.new { 0 }

      site.data['videos'].each{|k, v|
        if ! v.nil?
          v.fetch('tags', []).each{|tag|
            v.fetch('versions', []).each{|version|
              durations['bytag'][tag] += findDuration(version['length']) / 3600.0
              durations['_total_'] += findDuration(version['length']) / 3600.0
              version['speakers'].each{|speaker|
                durations['byspeaker'][speaker] += findDuration(version['length']) / 3600.0
              }
              if version['captions']
                version['captions'].each{|speaker|
                  durations['bycaptioner'][speaker] += findDuration(version['length']) / 3600.0
                }
              end
            }
          }
        end
      }
      site.data['stats'] = durations
      durations['bytag'] = durations['bytag'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}
      durations['byspeaker'] = durations['byspeaker'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}
      durations['bycaptioner'] = durations['bycaptioner'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}
    end
  end
end

