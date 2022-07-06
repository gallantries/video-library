#!/usr/bin/env ruby
require 'pp'
require 'yaml'
require 'find'
require 'pathname'
require 'kwalify'

# Schemas
EVENT_SCHEMA = YAML.load_file('bin/schema-event.yaml')
VIDEO_SCHEMA = YAML.load_file('bin/schema-videos.yaml')

# Contributors
CONTRIBUTORS = YAML.load_file('_data/instructors.yaml')
VIDEOS = YAML.load_file('_data/videos.yaml')
SESSIONS = YAML.load_file('_data/sessions.yaml')

# Update the existing schemas to have enums with values. Then we get validation
# *for free*!
EVENT_SCHEMA['mapping']['instructors']['sequence'][0]['enum'] = CONTRIBUTORS.keys
EVENT_SCHEMA['mapping']['contacts']['sequence'][0]['enum'] = CONTRIBUTORS.keys
EVENT_SCHEMA['mapping']['program']['mapping']['=']['mapping']['trainings']['sequence'][0]['mapping']['video']['enum'] = VIDEOS.keys
EVENT_SCHEMA['mapping']['program']['mapping']['=']['mapping']['trainings']['sequence'][0]['mapping']['session']['enum'] = SESSIONS.keys
EVENT_SCHEMA['mapping']['program']['mapping']['=']['mapping']['trainings']['sequence'][0]['mapping']['instructors']['sequence'][0]['enum'] = CONTRIBUTORS.keys

# Build validators now that we've filled out the subtopic enum
$event_validator = Kwalify::Validator.new(EVENT_SCHEMA)

def validate_document(document, validator)
  errors = validator.validate(document)
  if errors && !errors.empty?
    return errors
  end
  return []
end


def lint_file(fn)
  # Any error messages
  errs = []

  begin
    data = YAML.load_file(fn)
  rescue
    puts "Skipping #{fn}"
    return nil
  end

  # Check this is something we actually want to process
  if ! data.is_a?(Hash) then
    puts "Skipping #{fn}"
    return nil
  end

  # Skip non-events
  if data['layout'] != 'event'
    puts "Skipping #{fn}"
    return nil
  end

  # Generic error handling:
  errs.push(*validate_document(data, $event_validator))

  # If we had no errors, validated successfully
  if errs.length == 0 then
    #puts "\e[38;5;40m#{fn} validated succesfully\e[m"
  else
    # Otherwise, print errors and exit non-zero
    puts "\e[48;5;09m#{fn} has errors\e[m"
    errs.each {|x| puts "  #{x}" }
  end
  return errs
end


ec = 0
Find.find('./events') do |path|
  if FileTest.directory?(path)
    if File.basename(path).start_with?('.')
      Find.prune       # Don't look any further into this directory.
    else
      next
    end
  else
    last_component = path.split('/')[-1]
    if last_component =~ /.*\.md/ || last_component =~ /.*\.html/ then
      errs = lint_file(path)
      if !errs.nil? && errs.length > 0 then
        ec = 1
      end
    end
  end
end

exit ec
