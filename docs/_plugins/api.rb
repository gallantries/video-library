require 'json'

module Jekyll
  class APIGenerator < Generator

    def findDuration(duration)
      eval(duration.gsub(/H/, ' * 3600 + ').gsub(/M/, ' * 60 + ').gsub(/S/, ' + ') + " 0")
    end

    def write_api_json(site, path, data)
      page2 = PageWithoutAFile.new(site, "", "api/", path)
      page2.content = JSON.pretty_generate(data)
      page2.data["layout"] = nil
      site.pages << page2
    end

    def generate(site)
      puts "[VideoLibrary/API] Videos & Sessions"
      write_api_json(site, "gtn.json", site.data['gtn'])
      write_api_json(site, "studyload.json", site.data['studyload'])
      write_api_json(site, "instructors.json", site.data['instructors'])
      write_api_json(site, "affiliations.json", site.data['affiliations'])

      by_tags = Hash.new { |hash, key| hash[key] = Hash.new }
      site.data['videos'].each{|k, v|
        if ! v.nil?
          v.fetch('tags', []).each{|tag|
            by_tags[tag]['url'] = site.config['baseurl'] + "/api/tags/#{tag}.json"
            if by_tags[tag]['videos'].nil?
              by_tags[tag]['videos'] = Hash.new
            end

            gtn_id = k.split('/')[0..1].join('/')
            v['gtn_id'] = gtn_id

            if ! v.has_key?("title")
              v['title'] = v.fetch('name', site.data['gtn'].fetch(gtn_id, k))
            end

            if v.fetch('versions', []).length > 0
              if v['versions'][0]['captions'].nil? then
                v['captioned'] = false
              else
                v['captioned'] = v['versions'][0].fetch('captions', []).length > 0
              end
            end

            by_tags[tag]['videos'][k] = v
          }
        end
      }

      write_api_json(site, "videos.json", site.data['videos'])
      write_api_json(site, "sessions.json", site.data['sessions'])

      site.data['by_tags'] = by_tags
      by_tags.each{ |tag, data|
        write_api_json(site, "tags/#{tag}.json", data)
      }

      by_youtube = Hash.new

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

        if v['versions']
          v['versions'].each{|vid|
            by_youtube[vid['link']] = k
          }
        end
      }

      by_material.each{ |tag, data|
        write_api_json(site, "by-material/#{tag}.json", data)
      }
      write_api_json(site, "by-material.json", by_material)
      write_api_json(site, "by-youtube.json", by_youtube)
      write_api_json(site, "tags.json", by_tags)

      # Stats
      durations = Hash.new { 0 }
      durations['bytag'] = Hash.new { 0 }
      durations['byspeaker'] = Hash.new { 0 }
      durations['bycaptioner'] = Hash.new { 0 }
      durations['_speakers_'] = []

      site.data['videos'].each{|k, v|

        k2 = k.split('/')[0,2].join('/')
        v['name'] = site.data['gtn'].fetch(k2, k2)

        if ! v.nil?
          v.fetch('tags', []).each{|tag|
            first = v.fetch('versions', []).first
            if ! first.nil? and ! first.empty? and ! first['length'].nil?
              durations['_total_latest_'] += findDuration(first['length']) / 3600.0
              durations['_total_latest_count_'] += 1
            end
            v.fetch('versions', []).each{|version|

              k2 = k.split('/')[0,2].join('/')
              version['name'] = site.data['gtn'].fetch(k2, k2)

              durations['bytag'][tag] += findDuration(version['length']) / 3600.0
              durations['_total_'] += findDuration(version['length']) / 3600.0
              durations['_total_count_'] += 1
              version['speakers'].each{|speaker|
                durations['_speakers_'].push(speaker)
                durations['byspeaker'][speaker] += findDuration(version['length']) / 3600.0 / version['speakers'].length
              }
              if version['captions']
                version['captions'].each{|speaker|
                  durations['_speakers_'].push(speaker)
                  durations['bycaptioner'][speaker] += findDuration(version['length']) / 3600.0 / version['captions'].length
                }
              end
            }
          }
        end
      }
      site.data['stats'] = durations

      durations['_speakers_count_'] = durations['_speakers_'].uniq.length - 2 # Galaxy Community, AWS Polly
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

      # Modules
      modules = Hash.new
      site.pages.select{|p| p['layout'] == 'module'}
        .select{|p| p.path =~ /module/} # Not fully sure why we need this
        .each{|page|

        p = page.path.gsub(/.md/, '.json')
        fn = p.split('/')[-1].gsub(/.json/, '')
        modules[fn] = page.data.dup
        modules[fn]['url'] = site.config['url'] + site.config['baseurl'] + '/api/' + p

        write_api_json(site, p, page.data)

      }
      write_api_json(site, "modules.json", modules)


      # Events
      site.pages.select{|p| p['layout'] == 'event'}.each{|page|
        p = page.path.gsub(/.md/, '.json')
        path = ['api'] + p.split('/')[0..-2]
        fn = p.split('/')[-1]
        page2 = PageWithoutAFile.new(site, "", path.join('/'), fn)
        pd = page.data.dup
        pd['content'] = '{% raw %}\n' + page.content + '{% endraw %}'
        if pd.has_key?('url') then
          pd.delete('url')
        end
        page2.content = JSON.pretty_generate(pd)
        page2.data["layout"] = nil
        site.pages << page2
      }
    end
  end
end

