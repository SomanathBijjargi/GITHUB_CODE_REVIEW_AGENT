import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";

function Reviews() {

  const [reviews, setReviews] =
    useState([]);

  useEffect(() => {

    api
      .get("/reviews")
      .then((res) => {
        setReviews(res.data);
      });

  }, []);

  return (
    <div className="bg-white p-6 rounded-xl shadow mb-8">

      <h1>
        Review History
      </h1>

      {
        reviews.map(
          (review, index) => (

            <Link to={`/reviews/${review.pr_number}`}>

              <h3>
                PR #
                {review.pr_number}
              </h3>

              <p>
                Repo:
                {review.repo}
              </p>

              <p>
                Title:
                {review.pr_title}
              </p>

            </Link>
          )
        )
      }

    </div>
  );
}

export default Reviews;