import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../services/api";

function ReviewDetails() {

  const { prNumber } = useParams();

  const [data, setData] =
    useState(null);

  useEffect(() => {

    api
      .get(`/reviews/${prNumber}`)
      .then((res) => {
        setData(res.data);
      });

  }, [prNumber]);

  if (!data)
    return <h2>Loading...</h2>;

  return (
    <div>

        <h1>
            PR #{data.pr_number}
        </h1>

        <h2>Summary</h2>
        <p>{data.review.summary}</p>

        <h2> Bugs </h2>
        {
            data.review.bugs?.length > 0
            ? data.review.bugs.map((bug, index) => (
                <div key={index}>
                    <p>
                    <strong>{bug.line}</strong>
                    </p>

                    <p>
                    {bug.description}
                    </p>

                    <p>
                    Severity: {bug.severity}
                    </p>
                </div>
                ))
            : <p>No bugs found</p>
        }

        <h2>🔒 Security Issues</h2>

        {
            data.review.security?.length > 0
            ? data.review.security.map((item, index) => (
                <div key={index}>
                    <p>
                    {item.issue}
                    </p>

                    <p>
                    Recommendation:
                    {" "}
                    {item.recommendation}
                    </p>
                </div>
                ))
            : <p>No security issues</p>
        }

        <h2>⚡ Performance Issues</h2>

        {
            data.review.performance?.length > 0
            ? data.review.performance.map((item, index) => (
                <div key={index}>
                    <p>{item.issue}</p>

                    <p>
                    Recommendation:
                    {" "}
                    {item.recommendation}
                    </p>
                </div>
                ))
            : <p>No performance issues</p>
        }

        <h2>📋 Quality Issues</h2>

        {
            data.review.quality?.length > 0
            ? data.review.quality.map((item, index) => (
                <div key={index}>
                    <p>{item.issue}</p>

                    <p>
                    Recommendation:
                    {" "}
                    {item.recommendation}
                    </p>
                </div>
                ))
            : <p>No quality issues</p>
        }


    </div>
  );
}

export default ReviewDetails;