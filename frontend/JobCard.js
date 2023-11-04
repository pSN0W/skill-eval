import React from 'react';
import './JobCard.css'; // Create a CSS file for styling
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMapMarkerAlt } from '@fortawesome/free-solid-svg-icons';

const JobCard = ({ date, jobName, location, numCandidates }) => {
  return (
    <div className="job-card">
      <div className="cyan-section">
        <div className="date"> {date}</div>
        <div className="job-name">{jobName}</div>
        <div className="location">
            <FontAwesomeIcon icon={faMapMarkerAlt} />
          <p style={{marginLeft: '1%'}}>
          {location}
          </p>
        </div>
      </div>
      <div className="bottom-section">
        <div className="num-candidates">
          Applied: {numCandidates}
        </div>
        <button class="button-27" role="button">View </button>
      </div>
    </div>
  );
};

export default JobCard;
