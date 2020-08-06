import React from "react";
import Canvas from "./Canvas.js"

export default class App extends React.Component {
    constructor(props){
        super(props);
        this.canvas;
    }
    render(){
        return(
            <div id="canvcont">
                <Canvas ref={(_canvas)=>{this.canvas = _canvas}} id="testCanvas" container="canvcont" width="800" height="800"></Canvas>
            </div>
        );
    }
    update(){}
}