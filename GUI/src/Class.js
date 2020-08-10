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
                <Card style={{width: 200, backgroundColor: '#aaaaff'}} bordered={false} hoverable >
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
});