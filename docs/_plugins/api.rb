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

      puts "[VideoLibrary/API] Sessions"
      page2 = PageWithoutAFile.new(site, "", "api/", "sessions.json")
      page2.content = JSON.pretty_generate(site.data['sessions'])
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
              durations['_total_count_'] += 1
              version['speakers'].each{|speaker|
                durations['byspeaker'][speaker] += findDuration(version['length']) / 3600.0 / version['speakers'].length
              }
              if version['captions']
                version['captions'].each{|speaker|
                  durations['bycaptioner'][speaker] += findDuration(version['length']) / 3600.0 / version['captions'].length
                }
              end
            }
          }
        end
      }
      site.data['stats'] = durations

      durations['bytag_a'] = durations['bytag'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}
      durations['byspeaker_a'] = durations['byspeaker'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}
      durations['bycaptioner_a'] = durations['bycaptioner'].map{|k, v| [k, v]}.sort_by{|a| -a[1]}

      # Propagate video tags to sessions
      site.data['sessions_bytag'] = Hash.new { Array.new }
      site.data['sessions'].each{|k, v|
        # For each session we have some videos:
        tags = v['videos'].map{|video| site.data['videos'][video]['tags'] }.flatten.uniq
        tags.each{|tag|
          if ! site.data['sessions_bytag'].has_key? tag
            site.data['sessions_bytag'][tag] = {}
          end
          site.data['sessions_bytag'][tag][k] = site.data['sessions'][k]
        }
      }
    end
  end
end

