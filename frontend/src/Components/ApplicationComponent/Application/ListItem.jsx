// ListItem.js
import React from "react";
import "./ListItem.css";

const ListItem = ({ name, email, score }) => {
  return (
    <div className="list-item">
      <div className="list-item-info">
        <div className="name">{name}</div>
        <div className="email">{email}</div>
      </div>
      {score != null && <div className="score">{score}</div>}
      {score == null && <div>Loading</div>}
    </div>
  );
};

export default ListItem;
