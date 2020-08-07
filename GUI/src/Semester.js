import React from "react";
import { useDrop } from "react-dnd";
import { Row, Col, Divider } from "antd"
import { Class } from "./Class"
import { MovableTypes } from "./MovableTypes";
import 'antd/dist/antd.css';

export function Semester (props) {
    const [{ isOver, canDrop }, drop] = useDrop({
        accept: MovableTypes.CLASS,
        drop: () => {console.log("dropped in " + props.name)},
        collect: (mon) => ({
            isOver: !!mon.isOver(),
            canDrop: !!mon.canDrop()
        })
    })
    return (
        <div ref={drop}>
            <Divider>{props.name}</Divider>
            <Row gutter={16}>
                {props.children}
            </Row>
        </div>
    )
}