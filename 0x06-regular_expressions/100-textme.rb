#!/usr/bin/env ruby
puts ARGV[0].scan(/(?:from:|to:|flags:)(\+?\w+|[-?\d:?]{5,})/).join(',')
