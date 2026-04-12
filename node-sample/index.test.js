const { add, greet } = require('./index');

test('1 + 2 は 3 になる', () => {
  expect(add(1, 2)).toBe(3);
});

test('挨拶メッセージが正しい', () => {
  expect(greet('田中')).toBe('こんにちは、田中さん！');
});
