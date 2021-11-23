#!/usr/bin/env ruby
require 'yaml'
require 'find'
require 'pathname'
require 'kwalify'

# Schemas
TOPIC_SCHEMA = YAML.load_file('bin/schema-videos.yaml')
CONTRIBUTORS = YAML.load_file('_data/instructors.yaml')

# Update the existing schemas to have enums with values. Then we get validation
# *for free*!
TOPIC_SCHEMA['mapping']['=']['mapping']['versions']['sequence'][0]['mapping']['captions']['sequence'][0]['enum'] = CONTRIBUTORS.keys
TOPIC_SCHEMA['mapping']['=']['mapping']['versions']['sequence'][0]['mapping']['speakers']['sequence'][0]['enum'] = CONTRIBUTORS.keys

# Build validators now that we've filled out the subtopic enum
$topic_validator = Kwalify::Validator.new(TOPIC_SCHEMA)


def validate_document(document, validator)
  errors = validator.validate(document)
  if errors && !errors.empty?
    return errors
  end
  return []
end

def validate_non_empty_key_value(map, key)
    if map.key?(key) then
      if map[key].length == 0 then
        return ["Empty #{key} for requirement"]
      end
    else
      return ["Missing #{key} for requirement"]
    end
    return []
end


data = YAML.load_file('_data/videos.yaml')
errs = validate_document(data, $topic_validator)
errs.each{|x| puts "#{x}"}
if errs.length > 0
  exit 1
end
