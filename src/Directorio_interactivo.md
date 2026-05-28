---
title: Página de pruebas
draft: false
toc: false
---

# Página de pruebas


### Texto "escondido"


<details>
  <summary>Click me</summary>
  This text is not visible by default.
</details>


### Texto "dentro de un recuadro y en negritas y cursiva"

<div class="grid grid-cols-4">
  <div class="card">

This is **Markdown** inside of _HTML_!

  </div>
</div>

### Grids

<div class="grid grid-cols-4">
  <div class="card"><h1>A</h1></div>
  <div class="card"><h1>B</h1></div>
  <div class="card"><h1>C</h1></div>
  <div class="card"><h1>D</h1></div>
</div>

Una cuadricula con diferentes tamaños de recuadros


<div class="grid grid-cols-2">
  <div class="card"><h1>A</h1>1 × 1</div>
  <div class="card grid-rowspan-2"><h1>B</h1>1 × 2</div>
  <div class="card"><h1>C</h1>1 × 1</div>
  <div class="card grid-colspan-2"><h1>D</h1>2 × 1</div>
</div>



Con texto sería algo del estilo:
<div class="grid grid-cols-2">
  <div class="card">Call me Ishmael.</div>
  <div class="card">Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.</div>
  <div class="card">It is a way I have of driving off the spleen and regulating the circulation.</div>
</div>

### Cards

Se usa normalmente para agrupar y delimitar contenido con colores **determinados por el tema actual**

<div class="card" style="max-width: 640px;">
  <h2>It gets hotter during summer</h2>
  <h3>And months have 28–31 days</h3>
  ${Plot.cell(weather.slice(-365), {x: (d) => d.date.getUTCDate(), y: (d) => d.date.getUTCMonth(), fill: "temp_max", tip: true, inset: 0.5}).plot({marginTop: 0, height: 240, padding: 0})}
</div>


#### Las cards se pueden usar por su cuenta pero normalmente existen en un "grid":

<div class="grid grid-cols-2">
  <div class="card">
    <h2>Lorem ipsum</h2>
    <p>Id ornare arcu odio ut sem nulla pharetra. Aliquet lectus proin nibh nisl condimentum id venenatis a. Feugiat sed lectus vestibulum mattis ullamcorper velit. Aliquet nec ullamcorper sit amet. Sit amet tellus cras adipiscing. Condimentum id venenatis a condimentum vitae. Semper eget duis at tellus. Ut faucibus pulvinar elementum integer enim.</p>
    <p>Et malesuada fames ac turpis. Integer vitae justo eget magna fermentum iaculis eu non diam. Aliquet risus feugiat in ante metus dictum at. Consectetur purus ut faucibus pulvinar.</p>
  </div>
  <div class="card" style="padding: 0;">
    ${Inputs.table(industries)}
  </div>
</div>

### Notes


<div class="note">This is a note.</div>

<div class="tip">This is a tip.</div>

<div class="warning">This is a warning.</div>

<div class="caution">This is a caution.</div>

Diferencias entre usar markdown y HTML:


#### HTML
<div class="tip">
  <p>This is a <i>styled</i> tip using <small>HTML</small>.</p>
</div>


#### Markdown

<div class="tip">

This is a *styled* tip using **Markdown**.

</div>

Se pueden:
<div class="warning" label="⚠️ Danger ⚠️">No lifeguard on duty. Swim at your own risk!</div>

<div class="note" label>This note has no label.</div>

### Tables

Column 1   | Column 2     | Column 3
---------- | ------------ | ----------
Cell 1-1   | Cell 2-1     | Cell 3-1
Cell 1-2   | Cell 2-2     | Cell 3-2

### Lists

- red
- green
- blue
  - light blue
  - dark blue

Enumeradas

1. first
1. second
1. third
   1. third first
   1. third second

### Links
<https://example.com>
[external link](https://example.com)
[external link](<https://en.wikipedia.org/wiki/Tar_(computing)>)

