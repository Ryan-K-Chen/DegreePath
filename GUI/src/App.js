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
                "Workspace": ["brep"],
                "Trash": [],
                "Fall 2019": ["bep"],
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
                                width={500} 
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
                                        treeData={courses_tree}
                                        onSelect={(e)=>{this.handleSelect(e)}}
                                        style={{
                                            width: "100%"
                                        }}
                                    >
                                    </TreeSelect>
                                    <Semester onDrop={(e)=>{this.handleDrop(e)}}>
                                        <div style={{
                                            minHeight: "100px"
                                        }}>
                                            {this.state.semesters["Workspace"].map(c => (
                                                <Class onDrag={(e)=>{this.handleDrag(e)}}></Class>
                                            ))}
                                        </div>                                        
                                    </Semester>
                                </div>
                            </Sider>
                            <Layout className="site-background" style={{
                                padding: "2vh 2vh 2vh", 
                                marginLeft: 500, 
                                minHeight: "100vh"
                            }}>
                                <Content className="class-content" style={{
                                    padding: "2vh",
                                    minHeight: "96vh"
                                }}>
                                    {Object.keys(this.state.semesters).map(s => (
                                        <Semester key={s} name={s} onDrop={(e)=>{this.handleDrop(e)}}>
                                            <div style={{
                                                minHeight: "100px"
                                            }}>
                                                {this.state.semesters[s].map(c => (
                                                    <Class key={c} name={c} onDrag={(e)=>{this.handleDrag(e)}}></Class>
                                                ))}
                                            </div>
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
        new_semesters[e[0]] = _.concat(new_semesters[e[0]], e[1]);
        this.setState({
            semesters: new_semesters
        });
    }
    handleSelect(e){
        console.log(e);
    }
    updateElement(){
        this.setState(this.state);
    }
}