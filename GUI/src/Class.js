import React from "react";
import { DragSource } from "react-dnd";
import { Col, Card } from "antd";
import { MovableTypes } from "./MovableTypes";
import 'antd/dist/antd.css';

const spec = {
    beginDrag(props, monitor, component) {
        props.onDrag(props.name);
        return component.props;
    }
}

const collect = (connect, monitor) => {
    return {
        connectDragSource: connect.dragSource()
    }
}

export const Class = DragSource(MovableTypes.CLASS, spec, collect) (class extends React.Component {
    constructor(props){
        super(props);
        console.log("Here:")
        console.log(props);
    }
    render(){
        const {connectDragSource} = this.props;
        return (connectDragSource(
            <div>
                <Col>
                <Card style={{width: 200, backgroundColor: '#B4A76C'}} bordered={false} hoverable onMouseEnter={()=>{this.handleMouseEnter()}} onMouseLeave={()=>{this.handleMouseExit()}}>
                    <h2>
                    <b>
                        <center>
                            {this.props.name}
                        </center>
                    </b>
                    </h2>
                </Card>
                </Col>
            </div>
        ));
    }
    handleMouseEnter(){
        console.log("entered on " + this.props.name)
    }
    handleMouseExit(){
        console.log("exited on " + this.props.name)
    }
});