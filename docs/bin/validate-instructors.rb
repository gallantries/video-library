#!/usr/bin/env ruby
require 'yaml'
require 'find'
require 'pathname'
require 'kwalify'

# Schemas
INSTRUCTORS_SCHEMA = YAML.load_file('bin/schema-instructors.yaml')
AFFILIATIONS_SCHEMA = YAML.load_file('bin/schema-institutions.yaml')
INSTITUTIONS = YAML.load_file('_data/affiliations.yaml')
PICTURES = Dir["assets/images/logos/*"].map{|x| x["assets/images/logos/".length..-1]}
PICS_PEOPLE = Dir["assets/images/instructors/*"].map{|x| x["assets/images/instructors/".length..-1]}

# Update the existing schemas to have enums with values. Then we get validation
# *for free*!
INSTRUCTORS_SCHEMA['mapping']['=']['mapping']['affiliation']['sequence'][0]['enum'] = INSTITUTIONS.keys
INSTRUCTORS_SCHEMA['mapping']['=']['mapping']['photo']['enum'] = PICS_PEOPLE
AFFILIATIONS_SCHEMA['mapping']['=']['mapping']['logo']['enum'] = PICTURES

# Build validators now that we've filled out the subtopic enum
$instructor_validator = Kwalify::Validator.new(INSTRUCTORS_SCHEMA)
$affiliation_validator = Kwalify::Validator.new(AFFILIATIONS_SCHEMA)


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


data = YAML.load_file('_data/instructors.yaml')
errs = validate_document(data, $instructor_validator)

data2 = YAML.load_file('_data/affiliations.yaml')
errs += validate_document(data2, $affiliation_validator)



errs.each{|x| puts "#{x}"}
if errs.length > 0
  exit 1
end
