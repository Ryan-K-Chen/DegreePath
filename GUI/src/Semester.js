import React from "react";
import { DropTarget } from "react-dnd";
import { Row, Col, Divider } from "antd"
import { Class } from "./Class";
import { MovableTypes } from "./MovableTypes";
import _ from "lodash";
import 'antd/dist/antd.css';

const spec = {
    drop(props, monitor, component) {
        const item = monitor.getItem();
        component.onDrop(item);
        return item;
    }
}

const collect = (connect, monitor) => {
    return {
        connectDropTarget: connect.dropTarget()
    }
}

export const Semester = DropTarget(MovableTypes.CLASS, spec, collect) ( class extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            classes: []
        }
    }
    render(){
        const {connectDropTarget} = this.props;
        return (connectDropTarget(
            <div>
                <Divider>{this.props.name}</Divider>
                <Row gutter={16}>
                    {/* {this.state.classes.map(c => (
                        <Class key={c} name={c}></Class>
                    ))} */}
                    {this.props.children}
                </Row>
            </div>
        ))
    }
    onDrop(item){
        console.log("you dropped this king: " + item.props.name);
        const newclasses = _.concat(_.filter(this.state.classes, (o)=>{return o!=item.props.name}), item.props.name);
        this.setState({
            classes: newclasses
        });
    }
});