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
        props.onDrop([component.props.name, item.name]);
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
    }
    render(){
        const {connectDropTarget} = this.props;
        if(this.props.credits === ""){
            return (connectDropTarget(
                <div>
                    <Divider style={{fontSize: "20px", fontFamily: "monospace"}}>{this.props.name}</Divider>
                    <Row gutter={[16,16]} justify="center" style={{
                        minHeight: this.props.minHeight
                    }}>
                        {this.props.children}
                    </Row>
                </div>
            ))
        } else {
            return (connectDropTarget(
                <div>
                    <Divider style={{fontSize: "20px", fontFamily: "monospace"}}>{this.props.name + " (" + this.props.credits + ")"}</Divider>
                    <Row gutter={[16,16]} justify="center" style={{
                        minHeight: this.props.minHeight
                    }}>
                        {this.props.children}
                    </Row>
                </div>
            ))
        }
    }
});

Semester.defaultProps = {
    minHeight: "120px"
}