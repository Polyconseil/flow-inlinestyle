# flow-inlinestyle

To statically check your style objects

## How to use ?

First:
`npm install --save-dev flow-inlinestyle`

And then in you .flowconfig:
```
[libs]
node_modules/flow-inlinestyle/
```

And the in your code:
```javascript
const STYLE_FOO: InlineStyle = {
  marginRight: 10,
  display: 'inline-block',
};
```
