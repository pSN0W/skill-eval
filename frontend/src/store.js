import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import { hrLoginReducer } from "./Reducers/hrReducers";
import { jobsListReducer } from "./Reducers/jobReducers";
import { applicationsListReducer } from "./Reducers/applicationReducers";

const reducer = combineReducers({
    hrLogin: hrLoginReducer,
    jobList: jobsListReducer,
    applicationList: applicationsListReducer
})

const initialState = {};
const middleware = [thunk];
const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;