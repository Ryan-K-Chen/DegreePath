import React from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { Class } from "./Class"
import { Semester } from "./Semester"
import 'antd/dist/antd.css';



export default class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            semesters: {
                "Fall 2019": ["ye", "he"],
                "Spring 2020": [],
                "Summer 2020": [],
                "Fall 2020": []
            }
        }
    }
    render(){
        return (
            <div>
                <DndProvider backend={HTML5Backend}>
                    <Class name="ECE 2020"></Class>
                    <Class name="BEP 2010"></Class>
                    {Object.keys(this.state.semesters).map(s => (
                        <Semester key={s} name={s}>
                            {this.state.semesters[s].map(c => (
                                <Class key={c} name={c}></Class>
                            ))}
                        </Semester>
                    ))}
                </DndProvider>
            </div>
        );
    }
}