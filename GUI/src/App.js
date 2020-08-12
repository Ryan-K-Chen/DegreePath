import React from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { Layout, TreeSelect } from "antd";
import { Class } from "./Class";
import { Semester } from "./Semester";
import { courses_tree } from "./data/courses_tree.json";
import 'antd/dist/antd.css';
import './App.css'

const { Header, Content, Footer, Sider } = Layout;
const { TreeNode } = TreeSelect;

export default class App extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            semesters: {
                "Workspace": [],
                "Trash": [],
                "Fall 2019": ["ECE 2020"],
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
                                    Add a Class:
                                    <br/>
                                    <TreeSelect
                                        showSearch
                                        placeholder={"Add a Class to the Workspace"}
                                        treeData={courses_tree}
                                        onSelect={(e)=>{this.handleSelect(e)}}
                                        style={{
                                            width: "100%"
                                        }}
                                    >
                                    </TreeSelect>
                                    <Semester name={"Workspace"} justify="space-around" onDrop={(e)=>{this.handleDrop(e)}}>
                                        {this.state.semesters["Workspace"].map(c => (
                                            <Class name={c} key={c} onDrag={(e)=>{this.handleDrag(e)}}></Class>
                                        ))}
                                    </Semester>
                                    <Semester name={"Trash"} onDrop={(e)=>{this.handleDrop(e)}}>

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
                                    {_.filter(Object.keys(this.state.semesters), (o)=>{return !(o=="Workspace" || o=="Trash")}).map(s => (
                                        <Semester key={s} name={s} onDrop={(e)=>{this.handleDrop(e)}}>
                                            {this.state.semesters[s].map(c => (
                                                <Class key={c} name={c} onDrag={(e)=>{this.handleDrag(e)}}></Class>
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
            new_semesters[key] = _.filter(value, (o)=>{return o!=e[1]});
        });
        if(e[0] != "trash"){
            new_semesters[e[0]] = _.concat(new_semesters[e[0]], e[1]);
        }
        this.setState({
            semesters: new_semesters
        });
    }
    handleSelect(e){
        console.log(e);
        const new_semesters = this.state.semesters;
        _.forEach(this.state.semesters, (value, key) => {
            new_semesters[key] = _.filter(value, (o)=>{return o!=e});
        });
        new_semesters["Workspace"] = _.concat(new_semesters["Workspace"], e);
        this.setState({
            semesters: new_semesters
        });
    }
    updateElement(){
        this.setState(this.state);
    }
}