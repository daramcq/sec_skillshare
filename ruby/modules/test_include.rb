require_relative 'utilities_with_include'

class TestInclude
  include ::UtilitiesWithInclude

  def perform(text)
    pretty_print(text)
  end
end


TestInclude.new.perform("Hello I am text prettified with an included module")
