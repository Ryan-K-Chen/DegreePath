import React from "react";
import { useDrag } from "react-dnd";
import { Col, Card } from "antd";
import { MovableTypes } from "./MovableTypes";
import 'antd/dist/antd.css';

export function Class (props) {
    const [{ isDragging }, drag] = useDrag({
        item: { type: MovableTypes.CLASS },
        collect: (monitor) => ({
            isDragging: !!monitor.isDragging()
        })
    })
    return (
        <div ref={drag}>
            <Col>
            <center>
            <Card style={{width: 200, backgroundColor: '#aaaaff'}} bordered={false} hoverable >
                <h2>
                <b>
                    <center>
                        {props.name}
                    </center>
                </b>
                </h2>
            </Card>
            </center>
            </Col>
        </div>
    );
}