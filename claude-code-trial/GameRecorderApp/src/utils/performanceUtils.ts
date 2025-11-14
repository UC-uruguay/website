import { InteractionManager } from 'react-native';

export class PerformanceUtils {
  private static performanceMarks: Map<string, number> = new Map();

  static startMeasure(name: string): void {
    this.performanceMarks.set(name, performance.now());
  }

  static endMeasure(name: string): number {
    const startTime = this.performanceMarks.get(name);
    if (!startTime) {
      console.warn(`Performance measure '${name}' was not started`);
      return 0;
    }

    const duration = performance.now() - startTime;
    this.performanceMarks.delete(name);
    
    console.log(`Performance: ${name} took ${duration.toFixed(2)}ms`);
    return duration;
  }

  static async runAfterInteractions<T>(task: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      InteractionManager.runAfterInteractions(async () => {
        try {
          const result = await task();
          resolve(result);
        } catch (error) {
          reject(error);
        }
      });
    });
  }

  static debounce<T extends (...args: any[]) => any>(
    func: T,
    delay: number
  ): (...args: Parameters<T>) => void {
    let timeoutId: NodeJS.Timeout;
    
    return (...args: Parameters<T>) => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => func(...args), delay);
    };
  }

  static throttle<T extends (...args: any[]) => any>(
    func: T,
    delay: number
  ): (...args: Parameters<T>) => void {
    let lastCall = 0;
    
    return (...args: Parameters<T>) => {
      const now = Date.now();
      if (now - lastCall >= delay) {
        lastCall = now;
        func(...args);
      }
    };
  }

  static measureComponentRender(componentName: string) {
    return {
      onRenderStart: () => {
        this.startMeasure(`${componentName}_render`);
      },
      onRenderEnd: () => {
        this.endMeasure(`${componentName}_render`);
      },
    };
  }

  static optimizeImageLoad(imageUri: string): string {
    // Add image optimization parameters
    // This would typically connect to a CDN or image optimization service
    if (imageUri.includes('http')) {
      return `${imageUri}?w=400&h=400&fit=cover&auto=compress`;
    }
    return imageUri;
  }

  static getMemoryWarning(): boolean {
    // Mock memory warning detection
    // In a real app, you would use native modules to check memory usage
    const mockMemoryUsage = Math.random() * 100;
    return mockMemoryUsage > 80; // Warning if usage > 80%
  }

  static logPerformanceMetrics() {
    const metrics = {
      timestamp: new Date().toISOString(),
      activeMarks: Array.from(this.performanceMarks.keys()),
      memoryWarning: this.getMemoryWarning(),
    };

    console.log('Performance Metrics:', metrics);
    return metrics;
  }

  static clearPerformanceMarks(): void {
    this.performanceMarks.clear();
  }
}

// Export utility functions for common use cases
export const measure = PerformanceUtils.startMeasure.bind(PerformanceUtils);
export const endMeasure = PerformanceUtils.endMeasure.bind(PerformanceUtils);
export const runAfterInteractions = PerformanceUtils.runAfterInteractions.bind(PerformanceUtils);
export const debounce = PerformanceUtils.debounce.bind(PerformanceUtils);
export const throttle = PerformanceUtils.throttle.bind(PerformanceUtils);