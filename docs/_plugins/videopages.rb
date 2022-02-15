module Jekyll
  class VideoPageGenerator < Generator
    safe true

    def generate(site)
      if site.layouts.key? 'video'
        dir = 'videos'

        site.data['videos'].each_key do |video|
          # Using PageWithoutAFile instead of a custom class which reads files
          # from disk each time, saves some time, but it is unclear how much
          # due to how the previous was accounted. But assuming 0.040s per page * 193 should be about 8 seconds.
          page2 = PageWithoutAFile.new(site, "", File.join(dir, video), "index.html")
          page2.content = nil
          id2 = video.split('/')[0,2].join('/')

          name = site.data['gtn'].fetch(id2, video)
          description = site.data['videos'].fetch(video)['description']

          # Their tutorials
          page2.data["video"] = video
          page2.data['videoname'] = name
          page2.data['title'] = "GTN Video: #{name}"
          page2.data['description'] = "#{description}"
          page2.data["layout"] = "video"

          site.pages << page2

          # The embedded version
          page2 = PageWithoutAFile.new(site, "", File.join(dir, video), "embed.html")
          page2.content = nil
          id2 = video.split('/')[0,2].join('/')

          name = site.data['gtn'].fetch(id2, video)
          description = site.data['videos'].fetch(video)['description']

          # Their tutorials
          page2.data["video"] = video
          page2.data['videoname'] = name
          page2.data['title'] = "GTN Video: #{name}"
          page2.data['description'] = "#{description}"
          page2.data["layout"] = "embed"

          site.pages << page2


        end
      end

      if site.layouts.key? 'session'
        dir = 'sessions'

        site.data['sessions'].each_key do |session|
          page2 = PageWithoutAFile.new(site, "", File.join(dir, session), "index.html")
          page2.content = nil
          id2 = session.split('/')[0,2].join('/')

          name = site.data['gtn'].fetch(id2, session)

          # Their tutorials
          page2.data['session'] = session
          page2.data['sessionname'] = name
          page2.data['title'] = "GTN Video: #{name}"
          page2.data['layout'] = "session"

          site.pages << page2
        end
      end


    end
  end
end
