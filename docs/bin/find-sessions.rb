require 'yaml'
require 'json'

videos = YAML.load(open("_data/videos.yaml").read)
sessions = YAML.load(open("_data/sessions.yaml").read)


potential = Hash.new { |hash, key| hash[key] = [] }

videos.keys.each{|v|
  q = v.split('/')[0..-2]
  w = q.join('/')
  potential[w].push(v)
}

potential.select!{|k, v| v.length > 1}
potential.select!{|k, v| k.count('/') > 0}
potential.select!{|k, v| ! sessions.keys.include? k }

fn = open("_data/sessions.yaml", "a")

result = {}
potential.each{|k, v|
  result[k] = {
    "name" =>  "TODO",
    "description" =>  "TODO",
    "videos" =>  v
  }
}
fn.write(YAML.dump(result))
