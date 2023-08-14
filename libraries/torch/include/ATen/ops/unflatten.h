#pragma once

// @generated by torchgen/gen.py from Function.h

#include <ATen/Context.h>
#include <ATen/DeviceGuard.h>
#include <ATen/TensorUtils.h>
#include <ATen/TracerMode.h>
#include <ATen/core/Generator.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <c10/util/Optional.h>



#include <ATen/ops/unflatten_ops.h>

namespace at {


// aten::unflatten.int(Tensor(a) self, int dim, int[] sizes) -> Tensor(a)
inline at::Tensor unflatten(const at::Tensor & self, int64_t dim, at::IntArrayRef sizes) {
    return at::_ops::unflatten_int::call(self, dim, sizes);
}

// aten::unflatten.Dimname(Tensor(a) self, Dimname dim, int[] sizes, Dimname[] names) -> Tensor(a)
inline at::Tensor unflatten(const at::Tensor & self, at::Dimname dim, at::IntArrayRef sizes, at::DimnameList names) {
    return at::_ops::unflatten_Dimname::call(self, dim, sizes, names);
}

}