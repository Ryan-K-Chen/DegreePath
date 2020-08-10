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
                    {Object.keys(this.state.semesters).map(s => (
                        <Semester key={s} name={s} onDrop={(e)=>{this.handleDrop(e)}}>
                            {this.state.semesters[s].map(c => (
                                <Class key={c} name={c} onDrag={(e)=>{this.handleDrag(e)}}></Class>
                            ))}
                        </Semester>
                    ))}
                </DndProvider>
            </div>
        );
    }
    handleDrag(e){
        console.log(e);
    }
    handleDrop(e){
        console.log(e);
        const new_semesters = this.state.semesters;
        _.forEach(this.state.semesters, (value, key) => {
            new_semesters[key] = _.filter(value, (o)=>{return o!=e[1]});
        });
        new_semesters[e[0]] = _.concat(new_semesters[e[0]], e[1]);
        this.setState({
            semesters: new_semesters
        });
    }
}