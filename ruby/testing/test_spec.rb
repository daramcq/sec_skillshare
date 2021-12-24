require 'minitest/autorun'

class Calculator
  def add(x, y)
    x + y
  end

  def subtract(x, y)
    x - y
  end

  def equal?(x, y)
    x == y
  end
end

describe 'Calculator' do
  let(:calculator) { Calculator.new }

  describe '#add' do
    it 'adds numbers' do
      expect(calculator.add(4, 3)).must_equal 7
    end
  end

  describe '#subtract' do
    it 'subtracts numbers' do
      expect(calculator.subtract(10, 2)).must_equal 8
    end
  end

  describe '#equal?' do
    describe 'when numbers are equal' do
      it 'is true' do
        expect(calculator.equal?(5, 5)).must_equal true
      end
    end

    describe 'when numbers are not equal' do
      it 'is false' do
        expect(calculator.equal?(5, 6)).must_equal false
      end
    end
  end
end
