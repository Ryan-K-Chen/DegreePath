import React from "react"
import ReactDOM from "react-dom"
import App from "./App"
import { Class } from "./Class"
import { Button } from "antd"
import 'antd/dist/antd.css';
import { DndProvider } from "react-dnd"
import { HTML5Backend } from "react-dnd-html5-backend"
import { Semester } from "./Semester"

// let app = ReactDOM.render(<App />, document.getElementById("app"));

var semesters = [
    {
        name: "Fall 2019",
        classes: []
    },
    {
        name: "Spring 2020",
        classes: []
    }
];

let test = (
    <div>
        <DndProvider backend={HTML5Backend}>
            <Semester name="Fall 2020">
                <Class name="Class 1"></Class>
                <Class name="Class 2"></Class>
            </Semester>
            <Semester name="Spring 2020">
                <Class name="Class 3"></Class>
                <Class name="Class 4"></Class>
            </Semester>
        </DndProvider>
    </div>
);

ReactDOM.render(test, document.getElementById("app"));

