float WeightedAve(float input1, float input2, float weight1, float weight2){
  return (((input1 * weight1) + (input2 * weight2)) / (weight1 + weight2));
}
