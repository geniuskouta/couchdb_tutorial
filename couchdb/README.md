## CouchDB Design Documents

### How to access the database admin
- Access at http://localhost:5984/_utils/

### room_status database

1. **`_design/timestamp_view`**
   - **Purpose:** Provides a view for querying documents by their timestamp.
   - **View Definition:**
     ```json
     {
       "_id": "_design/timestamp_view",
       "views": {
         "by_timestamp": {
           "map": "function (doc) { if (doc.timestamp) { emit(doc.timestamp, doc); } }"
         }
       }
     }
     ```
