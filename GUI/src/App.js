import React from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";

export default class App extends React.Component {
    constructor(props){
        super(props);
        this.canvas;
    }
    render(){
        return(
            <div>
                <DndProvider backend={HTML5Backend}>
                    <div>

                    </div>
                </DndProvider>
            </div>
        );
    }
    update(){}
}