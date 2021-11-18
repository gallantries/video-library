#!/usr/bin/env ruby
require 'yaml'
require 'json'

YAML.load_stream(STDIN) do |document|
    puts JSON.pretty_generate(document)
end
