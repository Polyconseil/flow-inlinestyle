# flow-inlinestyle

To statically check your style objects

## How to use ?

First:
`npm install --save-dev flow-inlinestyle`

Add the type in your .flowconfig file :
```
[libs]
node_modules/flow-inlinestyle/index.js
```

Then, to use the type in your code:
```javascript
const STYLE_FOO: InlineStyle = {
  marginRight: 10,
  display: 'inline-block',
};
```
