require_relative 'utilities'

class Test
  def perform(text)
    Utilities::Formatter.pretty_print(text)
  end
end


Test.new.perform('pretty text')
