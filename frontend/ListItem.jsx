// ListItem.js
import React from 'react';
import './ListItem.css';

const ListItem = ({ name, email, score }) => {
  return (
    <div className="list-item">
      <div className="list-item-info">
        <div className="name">{name}</div>
        <div className="email">{email}</div>
      </div>
          <div className="score">{score}</div>
          
    </div>
  );
};

export default ListItem;
