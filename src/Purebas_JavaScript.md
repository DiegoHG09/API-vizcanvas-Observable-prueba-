# Pruebas usando JavaScript

Son las primeras pruebas familiarizandome con JavaScript:

### FENCED CODE BLOCKS

Este tipo de bloques se suele utilizar para desplegar contenido como tablas o inputs.

Existen dos tipos de bloques de "código cercado", **Los bloques de expresion y los bloques de programación**

Si queremos que el codigo del js se muestre debemos usar "echo" despues de js:

#### Un bloque de expresion se ve como el siguiente:

El bloque de expresion siempre muetra el resultado

```js echo
1 + 2
```

#### Mientras que uno de programación es de este estilo:
```js echo
const foo = 1 + 2;
```
Notemos que con la semicoma no muestra directamente el resultado, se necesita usar "display":

```js echo
display(foo)
```

Si queremos mostrar el código sin ejecutarlo necesitamos usar "run=false"

```js run=false
1 + 2
```

```js echo
document.createTextNode("[insert chart here]") // some imagination required
```


```js echo

```

```js echo
function greeting(name) {
  return html`Hello, <i>${name}</i>!`;
}
```

```js echo
greeting("world")
```

```js echo
Plot.lineY(aapl, {x: "Date", y: "Close"}).plot({y: {grid: true}})
```