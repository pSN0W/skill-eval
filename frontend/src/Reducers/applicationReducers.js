import {
  APPLICATIONS_LIST_REQUEST,
  APPLICATIONS_LIST_FAIL,
  APPLICATIONS_LIST_SUCCESS,
  APPLICATIONS_CREATE_REQUEST,
  APPLICATIONS_CREATE_SUCCESS,
  APPLICATIONS_CREATE_FAIL,
} from "../Constants/applicationConstants";

// reducer to get the list of note related to a user
export const applicationsListReducer = (state = { applications: {desc:"", applicants: []} }, action) => {
  switch (action.type) {
    case APPLICATIONS_LIST_REQUEST:
      return { loading: true, applications: {desc:"", applicants: []} };
    case APPLICATIONS_LIST_SUCCESS:
      return { loading: false, applications: action.payload };
    case APPLICATIONS_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export const applicationsCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case APPLICATIONS_CREATE_REQUEST:
      return { loading: true };
    case APPLICATIONS_CREATE_SUCCESS:
      return {
        loading: false,
        createdProduct: action.payload,
        success: true,
      };
    case APPLICATIONS_CREATE_FAIL:
      return { loading: false, error: action.payload, success: false };
    default:
      return state;
  }
};
