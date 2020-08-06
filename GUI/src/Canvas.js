import React from "react";

export default class Canvas extends React.Component {
    constructor(props){
        super(props);
        this.canvas;
        this.ctx;
        this.container;
    }
    render(){
        return(
            <canvas 
                id={this.props.id}
                onMouseDown={(e) => {this.mouseDown(e)}}
                onMouseUp  ={(e) => {this.mouseUp(e)}}
                onMouseMove={(e) => {this.mouseMove(e)}}
                width={this.props.width}
                height={this.props.height}
            />
        );
    }
    componentDidMount(){
        this.canvas = document.getElementById(this.props.id);
        this.ctx = this.canvas.getContext('2d');
        this.container = document.getElementById(this.props.container);

        let ctx = this;
        this.canvas.addEventListener('wheel',function(e){
			ctx.scroll(e);
			return false; 
		}, false);
    }
    resize(_width, _height){
		this.canvas.width = _width;
		this.canvas.height = _height;
    }
    fullscreen(){
        this.resize((this.container.offsetWidth),
					(window.innerHeight - this.container.offsetTop));
		this.resize((this.container.offsetWidth),
                    (window.innerHeight - this.container.offsetTop));
    }
    drawLine(_){
		this.ctx.beginPath();
		this.ctx.strokeStyle = _.strokeStyle;
		this.ctx.lineWidth = _.strokeWidth;
		this.ctx.setLineDash([0]);
		this.ctx.moveTo(_.x1, _.y1);
		this.ctx.lineTo(_.x2, _.y2);
		this.ctx.stroke();
	}
	drawDotted(_){
		this.ctx.beginPath();
		this.ctx.strokeStyle = _.strokeStyle;
		this.ctx.lineWidth = _.strokeWidth;
		this.ctx.setLineDash([6]);
		this.ctx.moveTo(_.x1, _.y1);
		this.ctx.lineTo(_.x2, _.y2);
		this.ctx.stroke();
	}
	drawCircle(_){
		this.ctx.beginPath();
		this.ctx.strokeStyle = _.strokeStyle;
		this.ctx.lineWidth = _.strokeWidth;
		this.ctx.arc(_.x, _.y, _.radius, 0, 2 * Math.PI);

		this.ctx.fillStyle = _.fillStyle;

		this.ctx.fill();
		this.ctx.stroke();
    }
    drawRect(_){
        this.ctx.beginPath();
		this.ctx.strokeStyle = _.strokeStyle;
        this.ctx.lineWidth = _.strokeWidth;
        this.ctx.rect(_.x,_.y,_.width,_.height);

		this.ctx.fillStyle = _.fillStyle;

		this.ctx.fill();
		this.ctx.stroke();
    }
    drawText(_){
		this.ctx.strokeStyle = _.strokeStyle;
		this.ctx.fillStyle = _.fillStyle;
        this.ctx.font = "30px Arial";
        this.ctx.fillText("Hello World", 10, 50);
    }
	color(_color){
		this.ctx.fillStyle = _color;
		this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
	}

    mouseDown(e){}
    mouseUp(e){}
    mouseMove(e){}
    scroll(e){}
}