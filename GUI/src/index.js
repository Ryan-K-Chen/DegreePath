import React from "react"
import ReactDOM from "react-dom"
import App from "./App.js"
import Class from "./Class.js"

let app = ReactDOM.render(<App />, document.getElementById("app"));

let classes = {};

console.log(app);

app.canvas.fullscreen();
let origwidth = app.canvas.canvas.width;
let origheight = app.canvas.canvas.height;


app.update = function () {
    app.canvas.fullscreen();
    app.canvas.color("#111111");
    app.canvas.drawRect({
					strokeStyle: "#0000ff",
                    strokeWidth: 3,
                    fillStyle: "#0000ff",
					x: 100, y: 100,
					width: (origwidth / 10), height: (origheight / 10)
                });
    app.canvas.drawText({
                    fillStyle: "#ffffff",
					x: 100, y: 100,
                });
    setTimeout(app.update, 20);
}

var timeout = setTimeout(app.update, 20);
