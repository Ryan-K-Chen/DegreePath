import React from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { Layout, TreeSelect, Button } from "antd";
import { Class } from "./Class";
import { Semester } from "./Semester";
import { courses_tree } from "./data/courses_tree.json";
import courses_dictionary from "./data/courses_dictionary.json"
import 'antd/dist/antd.css';
import './App.css'

const { Header, Content, Footer, Sider } = Layout;
const { TreeNode } = TreeSelect;


export default class App extends React.Component {
    constructor(props){
        super(props);
        let _state = JSON.parse(localStorage.getItem("AppState"));
        // if(_state == null){
        console.log(_state);
            let _sems = ["Fall 2019", "Spring 2020", "Summer 2020", "Fall 2020", "Spring 2021", "Summer 2021", "Fall 2021", "Spring 2022", "Summer 2022", "Fall 2022", "Spring 2023"];
            let _semesters = {
                "Workspace": {
                    "Courses": (_state["semesters"]["Workspace"] == null) ? [] : _state["semesters"]["Workspace"]["Courses"],
                    "Credits": 0
                },
                "Trash": {
                    "Courses": (_state["semesters"]["Trash"] == null) ? [] : _state["semesters"]["Trash"]["Courses"],
                    "Credits": 0
                },
                "Accredited Courses": {
                    "Courses": (_state["semesters"]["Accredited Courses"] == null) ? [] : _state["semesters"]["Accredited Courses"]["Courses"],
                    "Credits": 0
                },
            };
            _.forEach(_sems, (o)=>{
                _semesters[o] = {
                    "Courses": (_state["semesters"][o] == null) ? [] : _state["semesters"][o]["Courses"],
                    "Credits": 0
                }
            })
            console.log(_semesters);
            this.state = {
                sems: _sems,
                semesters: _semesters,
                satisfied: {}
            }
        console.log(this.state);
        // } else {
        //     this.state = _state;
        // }
    }
    render(){
        return (
            <div>
                <DndProvider backend={HTML5Backend}>
                    <Layout className="site-background">
                        <Layout>
                            <Sider 
                                width={600} 
                                className="class-sider"
                                style={{
                                    padding: "2vh 2vh 2vh",
                                    position: "fixed",
                                    height: "100vh"
                                }}>
                                <div className="class-sidercontent" style={{
                                    padding: "2vh",
                                    height: "96vh"
                                }}>
                                    <Button onClick={()=>{this.checkAllPrereqs()}}>Check All Prereqs</Button>
                                    <br/>
                                    Add a Class:
                                    <br/>
                                    <TreeSelect
                                        showSearch
                                        filterTreeNode={(e, v) => {return (v.title.toLowerCase().includes(e.toLowerCase()))}}
                                        placeholder={"Add a Class to the Workspace"}
                                        treeData={courses_tree}
                                        onSelect={(e)=>{this.handleSelect(e)}}
                                        listHeight={1024}
                                        style={{
                                            width: "100%"
                                        }}
                                    >
                                    </TreeSelect>
                                    <Semester name={"Workspace"} credits="" justify="space-around" onDrop={(e)=>{this.handleDrop(e)}}>
                                        {(this.state.semesters["Workspace"]["Courses"]).map(c => (
                                            <Class name={c} key={c} notsatisfied={false} onDrag={(e)=>{this.handleDrag(e)}}></Class>
                                        ))}
                                    </Semester>
                                    <Semester name={"Trash"} credits="" onDrop={(e)=>{this.handleDrop(e)}}>

                                    </Semester>
                                </div>
                            </Sider>
                            <Layout className="site-background" style={{
                                padding: "2vh 2vh 2vh", 
                                marginLeft: 600, 
                                minHeight: "100vh"
                            }}>
                                <Content className="class-content" style={{
                                    padding: "2vh",
                                    minHeight: "96vh"
                                }}>
                                    <Semester key={"Accredited Courses"} name={"Accredited Courses"} credits={this.state.semesters["Accredited Courses"]["Credits"]} onDrop={(e) => { this.handleDrop(e) }}>
                                        {(this.state.semesters["Accredited Courses"]["Courses"]).map(c => (
                                            <Class key={c} name={c} notsatisfied={false} onDrag={(e) => { this.handleDrag(e) }}></Class>
                                        ))}
                                    </Semester>
                                    {_.filter(Object.keys(this.state.semesters), (o)=>{return !(o=="Workspace" || o=="Trash" || o=="Accredited Courses")}).map(s => (
                                        <Semester key={s} name={s} credits={this.state.semesters[s]["Credits"]} onDrop={(e)=>{this.handleDrop(e)}}>
                                            {(this.state.semesters[s]["Courses"]).map(c => (
                                                <Class key={c} name={c} notsatisfied={!this.state.satisfied[c]} onDrag={(e)=>{this.handleDrag(e)}}></Class>
                                            ))}
                                        </Semester>
                                    ))}
                                </Content>
                            </Layout>
                        </Layout>
                    </Layout>
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
            new_semesters[key]["Courses"] = _.filter(value["Courses"], (o)=>{return o!=e[1]});
        });
        if(e[0] != "trash"){
            new_semesters[e[0]]["Courses"] = _.concat(new_semesters[e[0]]["Courses"], e[1]);
        }
        _.forEach(this.state.semesters, (value, key) => {
            new_semesters[key]["Credits"] = 0;
            _.forEach(new_semesters[key]["Courses"], (_value) => {
                new_semesters[key]["Credits"] = +new_semesters[key]["Credits"] + +courses_dictionary[_value]["Hours"]["Credit"]
            });
        });
        console.log(new_semesters)
        this.setState({
            semesters: new_semesters
        });
        this.checkAllPrereqs();
        this.updateLocalStorage();
    }
    handleSelect(e){
        const new_semesters = this.state.semesters;
        console.log(e);
        _.forEach(this.state.semesters, (value, key) => {
            new_semesters[key]["Courses"] = _.filter(value["Courses"], (o)=>{return o!=e});
        });
        new_semesters["Workspace"]["Courses"] = _.concat(new_semesters["Workspace"]["Courses"], e);
        this.setState({
            semesters: new_semesters
        });
        this.updateLocalStorage();
    }
    updateLocalStorage(){
        localStorage.setItem("AppState", JSON.stringify(this.state));
    }
    updateElement(){
        this.setState(this.state);
    }
    checkAllPrereqs(){ 
        let classes = [];
        classes = _.concat(classes, (this.state.semesters["Accredited Courses"]["Courses"]));
        let _state = this.state;
        _state.satisfied = {};
        _.forEach(this.state.sems, (o)=>{
            _.forEach(this.state.semesters[o]["Courses"], (cl) => {
                // console.log(o);
                let txt = courses_dictionary[cl]["Prerequisites"].toUpperCase();
                let pattern = new RegExp("\\w{2,4}[\\s]\\w{4,4}", "g") //the regular expression that finds class names within text
                let matches = txt.match(pattern); // returns an array with all class prerequisites
                let needToTake = []
                if(matches != null){
                    matches.forEach((item) => {
                        txt = txt.replace(item, (classes.includes(item)).toString());
                    }); //for each class prerequisite in the array, replace it in the string with true if taken, false if not (based on dictionary from DegreeWorks)
                } else {
                    txt = "true";
                }

                console.log(cl);
                console.log(txt);
                if (!eval(txt)) { //if they haven't returns a list of the prerequisites that have not been satisfied
                    matches.forEach((item) => {
                        if (!classes.includes([item])) {
                            needToTake.push(item);
                        }
                    });
                    // console.log("You have prerequisites that are currently unsatisfied: " + needToTake);
                    _state.satisfied[cl] = false;
                } else {
                    // console.log("satisfied!");
                    _state.satisfied[cl] = true;
                }
            });
            classes = _.concat(classes, (this.state.semesters[o]["Courses"]));
        });
        console.log(_state);
        this.setState(_state);
    }
}