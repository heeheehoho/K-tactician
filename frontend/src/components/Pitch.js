// Pitch.js (Conceptual Code)
import { useEffect, useRef } from 'react';
import * as d3 from 'd3';

const TacticalPitch = ({ events, ghostPath }) => {
  const svgRef = useRef();

  useEffect(() => {
    const svg = d3.select(svgRef.current);
    // 1. 축구장 라인 그리기
    // 2. 실제 패스 경로 (실선)
    // 3. What-if 경로 (점선 - Ghost Path)
    if (ghostPath) {
      svg.append("line")
         .attr("x1", ghostPath.start_x).attr("y1", ghostPath.start_y)
         .attr("x2", ghostPath.end_x).attr("y2", ghostPath.end_y)
         .attr("stroke", "rgba(255, 255, 255, 0.5)")
         .attr("stroke-dasharray", "5,5");
    }
  }, [ghostPath]);

  return <svg ref={svgRef} width={800} height={500} style={{background: '#224422'}} />;
};