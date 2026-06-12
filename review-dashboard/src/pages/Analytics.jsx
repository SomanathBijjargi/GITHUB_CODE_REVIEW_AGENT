import { useEffect, useState } from "react";
import api from "../services/api";
import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid
} from "recharts";

function Analytics() {

    const [stats, setStats] = useState(null);

    useEffect(() => {
        api
            .get("/stats")
            .then((res) => {
                setStats(res.data);
            });

    }, []);

    if (!stats)
        return <h2>Loading...</h2>;

    const scoreData = [
        {
            name: "Security",
            value: stats.average_security
        },
        {
            name: "Quality",
            value: stats.average_quality
        },
        {
            name: "Performance",
            value: stats.average_performance
        }
    ];

    const issueData = [
        {
            name: "Bugs",
            value: stats.total_bugs_found
        },
        {
            name: "Security",
            value: stats.total_security_issues
        }
    ];

    return (
        <div>

            <h1>Analytics</h1>

            <PieChart width={400} height={400}>
                <Pie data={scoreData} dataKey="value" outerRadius={120} label/> <Tooltip />
            </PieChart>

            <BarChart width={500}  height={300} data={issueData} >
                <CartesianGrid />
                <XAxis dataKey="name"/>
                <YAxis />
                <Tooltip />
                <Bar dataKey="value"/>
            </BarChart>
        </div>
    );
}

export default Analytics;