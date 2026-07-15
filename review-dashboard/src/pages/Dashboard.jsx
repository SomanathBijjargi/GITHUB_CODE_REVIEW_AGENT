import { useEffect, useState } from "react";
import api from "../services/api";
import StatCard from "../components/StatCard";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    api
      .get("/stats")
      .then((res) => setStats(res.data))
      .catch((err) => console.log(err));
  }, []);

  if (!stats) return <h2>Loading...</h2>;

  return (

  <div className="p-8">

    <h1
      className="
        text-4xl
        font-bold
        mb-8
      "
    >
      GitHub Review Analytics
    </h1>

    <div
      className="
        grid
        grid-cols-1
        md:grid-cols-2
        lg:grid-cols-3
        gap-6
      "
    >

      <StatCard
        title="Total Reviews"
        value={stats.total_reviews}
      />

      {/* <StatCard
        title="Bugs Found"
        value={stats.total_bugs_found}
      /> */}

      {/* <StatCard
        title="Security Issues"
        value={stats.total_security_issues}
      /> */}

      {/* <StatCard
        title="Average Security"
        value={stats.average_security}
      /> */}

      {/* <StatCard
        title="Average Quality"
        value={stats.average_quality}
      /> */}

      {/* <StatCard
        title="Average Performance"
        value={stats.average_performance}
      /> */}

      <StatCard
        title="Top Repository"
        value={stats.top_repository}
      />

      <StatCard
        title="Reviews This Week"
        value={stats.reviews_this_week}
      />

      <StatCard
        title="Reviews This Month"
        value={stats.reviews_this_month}
      />

    </div>

  </div>
);
}

export default Dashboard;