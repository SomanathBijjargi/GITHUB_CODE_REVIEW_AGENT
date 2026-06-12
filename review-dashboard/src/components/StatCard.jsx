function StatCard({ title, value }) {
  return (
    <div
      className="
        bg-white
        rounded-xl
        shadow-md
        p-6
        border
        hover:shadow-lg
        transition
      "
    >
      <h3
        className="
          text-gray-500
          text-sm
          font-medium
        "
      >
        {title}
      </h3>

      <h1
        className="
          text-3xl
          font-bold
          mt-2
        "
      >
        {value}
      </h1>
    </div>
  );
}

export default StatCard;