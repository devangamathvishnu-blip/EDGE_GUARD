export interface MLPrediction {
  anomaly_score: number;
  condition: string;
  current: number;
  machine_health: number;
  ml_status: string;
  prediction: string;
  risk: number;
  status: string;
  temperature: number;
  vibration: number;
  voltage: number;
}

export class MLDataProvider {
  private endpoint = "http://localhost:5000/api/predict";
  private pollTimer: ReturnType<typeof setInterval> | null = null;
  private latestData: MLPrediction | null = null;
  private subscribers: Array<(data: MLPrediction) => void> = [];
  private errorSubscribers: Array<(error: string) => void> = [];
  private isRunning = false;

  public start(): void {
    if (this.isRunning) return;
    this.isRunning = true;
    this.fetchPrediction();
    this.pollTimer = setInterval(() => this.fetchPrediction(), 1000);
  }

  public stop(): void {
    if (this.pollTimer !== null) {
      clearInterval(this.pollTimer);
      this.pollTimer = null;
    }
    this.isRunning = false;
  }

  public subscribe(callback: (data: MLPrediction) => void): () => void {
    this.subscribers.push(callback);
    if (this.latestData) callback(this.latestData);
    return () => {
      this.subscribers = this.subscribers.filter(s => s !== callback);
    };
  }

  public subscribeError(callback: (error: string) => void): () => void {
    this.errorSubscribers.push(callback);
    return () => {
      this.errorSubscribers = this.errorSubscribers.filter(s => s !== callback);
    };
  }

  private async fetchPrediction(): Promise<void> {
    try {
      const response = await fetch(this.endpoint, { cache: "no-store" });
      if (!response.ok) throw new Error(`ML server returned HTTP ${response.status}`);
      const data = await response.json();

      if (typeof data.machine_health !== "number" ||
          typeof data.anomaly_score !== "number") {
        throw new Error("Invalid ML response format");
      }

      this.latestData = data as MLPrediction;
      this.subscribers.forEach(cb => cb(this.latestData!));
    } catch (error: any) {
      const message = error?.message || "Unable to connect to ML server";
      console.error("EDGEGUARD ML CONNECTION ERROR:", message);
      this.errorSubscribers.forEach(cb => cb(message));
    }
  }
}
